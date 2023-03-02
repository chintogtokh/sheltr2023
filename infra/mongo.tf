# Config to run a one-instance MongoDB task. 

resource "aws_ecs_task_definition" "mongodb_task" {
  family                   = "mongodb-task"
  container_definitions    = <<DEFINITION
  [
    {
      "name": "mongodb-task",
      "image": "mongo:latest",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 27017,
          "hostPort": 27017
        }
      ],
      "environment": [
        {
          "name": "MONGO_INITDB_ROOT_USERNAME",
          "value": "${var.mongo_initdb_root_username}"
        },
        {
          "name": "MONGO_INITDB_ROOT_PASSWORD",
          "value": "${var.mongo_initdb_root_password}"
        },
        {
          "name": "MONGO_INITDB_ROOT_DATABASE",
          "value": "${var.mongo_initdb_root_database}"
        }
      ]
    }
  ]
  DEFINITION
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  memory                   = 512
  cpu                      = 256
  execution_role_arn       = aws_iam_role.ecsTaskExecutionRole.arn
}

resource "aws_ecs_service" "mongodb_service" {
  name            = "mongodb-service"
  cluster         = aws_ecs_cluster.sheltr_cluster.id
  task_definition = aws_ecs_task_definition.mongodb_task.arn
  launch_type     = "FARGATE"
  desired_count   = 1


  load_balancer {
    target_group_arn = aws_lb_target_group.lb_mongo_group.arn
    container_name   = aws_ecs_task_definition.mongodb_task.family
    container_port   = 27017
  }

  network_configuration {
    subnets          = ["${aws_default_subnet.default_subnet_a.id}", "${aws_default_subnet.default_subnet_b.id}", "${aws_default_subnet.default_subnet_c.id}"]
    assign_public_ip = true
    security_groups  = ["${aws_security_group.mongo_security_group.id}"]
  }
}

# This is honestly a waste of resources but it seemed like the most straightforward way to get a DNS
# record pointing to a Fargate service without using Service Discovery
resource "aws_lb" "mongo_elb" {
  name               = "mongo-elb"
  load_balancer_type = "network"
  subnets = [
    "${aws_default_subnet.default_subnet_a.id}",
    "${aws_default_subnet.default_subnet_b.id}",
    "${aws_default_subnet.default_subnet_c.id}"
  ]
}

resource "aws_lb_listener" "tcp" {
  load_balancer_arn = aws_lb.mongo_elb.id
  port              = 27017
  protocol          = "TCP"

  default_action {
    target_group_arn = aws_lb_target_group.lb_mongo_group.id
    type             = "forward"
  }
}

resource "aws_lb_target_group" "lb_mongo_group" {
  name        = "lb-mongo-group"
  port        = 27017
  protocol    = "TCP"
  target_type = "ip"
  vpc_id      = aws_default_vpc.default_vpc.id
  health_check {
    matcher = "200,301,302"
    path    = "/"
  }
}

resource "aws_security_group" "mongo_security_group" {
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Can be changed to only include ALB + Home Address, etc
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
