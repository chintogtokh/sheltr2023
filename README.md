# Sheltr
This is a MERN based app we made for a project at university.

The site is accessible from: https://pztest.chintogtokh.com , which was deployed using the config added here.

# Building and Deploying

The "system" consists of several parts:
* A React (legacy) frontend, which is bundled and pushed to s3 using a Github action (#1)
  * Very legacy, hasn't been touched in 5 years
* An ExpressJS app, which is containerised and pushed to ECS behind a load balancer using a Github action (#2)
  * In JS, but have modified parts of it to be more sane
* A MongoDB server, also containerised and pushed to ECR.
* A Github action (#3) to load data into the MongoDB database. The data itself is initially hosted on S3.
* Infrastructure, to set up the above into AWS and Cloudflare.
* Github: Secrets stored here

# More info

Please see the OLDREADME.md