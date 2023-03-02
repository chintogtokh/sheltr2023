# Sheltr API backend

resource "aws_ecs_task_definition" "sheltr_backend_task" {
  family                   = "sheltr-backend-task"
  container_definitions    = <<DEFINITION
  [
    {
      "name": "sheltr-backend-task",
      "image": "${aws_ecr_repository.sheltr_repo.repository_url}",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 4000,
          "hostPort": 4000
        }
      ],
      "environment": [
        {
          "name": "MONGO_DBHOST",
          "value": "${var.mongo_domain}"
        },
        {
          "name": "MONGO_DBPORT",
          "value": "27017"
        },
        {
          "name": "MONGO_DBNAME",
          "value": "sheltr"
        },
        {
          "name": "MONGO_DBUSER",
          "value": "${var.mongo_initdb_root_username}"
        },
        {
          "name": "MONGO_DBPASS",
          "value": "${var.mongo_initdb_root_password}"
        }
      ],
      "memory": 512,
      "cpu": 256
    }
  ]
  DEFINITION
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  memory                   = 512
  cpu                      = 256
  execution_role_arn       = aws_iam_role.ecsTaskExecutionRole.arn
}

resource "aws_ecs_service" "sheltr_backend_service" {
  name            = "sheltr-backend-service"
  cluster         = aws_ecs_cluster.sheltr_cluster.id
  task_definition = aws_ecs_task_definition.sheltr_backend_task.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  load_balancer {
    target_group_arn = aws_lb_target_group.target_group.arn
    container_name   = aws_ecs_task_definition.sheltr_backend_task.family
    container_port   = 4000
  }

  network_configuration {
    subnets          = ["${aws_default_subnet.default_subnet_a.id}", "${aws_default_subnet.default_subnet_b.id}", "${aws_default_subnet.default_subnet_c.id}"]
    assign_public_ip = true
    security_groups  = ["${aws_security_group.service_security_group.id}"]
  }
}

resource "aws_alb" "sheltr_backend_alb" {
  name               = "sheltr-backend-alb"
  load_balancer_type = "application"
  subnets = [
    "${aws_default_subnet.default_subnet_a.id}",
    "${aws_default_subnet.default_subnet_b.id}",
    "${aws_default_subnet.default_subnet_c.id}"
  ]
  security_groups = ["${aws_security_group.sheltr_backend_alb_security_group.id}"]
}

resource "aws_security_group" "sheltr_backend_alb_security_group" {
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_lb_target_group" "target_group" {
  name        = "target-group"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = aws_default_vpc.default_vpc.id
  health_check {
    matcher = "200,301,302"
    path    = "/"
  }
}

resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_alb.sheltr_backend_alb.arn
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target_group.arn
  }
}

resource "aws_security_group" "service_security_group" {
  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    # Only from sheltr_backend_alb_security_group
    security_groups = ["${aws_security_group.sheltr_backend_alb_security_group.id}"]
  }

  # Harden
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

