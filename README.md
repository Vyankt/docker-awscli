# Jenkins Docker AWS Production Project

## Tech Stack
- Jenkins
- Docker
- AWS EC2
- AWS ECR
- GitHub

## Flow
1. Code pushed to GitHub
2. Jenkins builds Docker image
3. Image pushed to ECR
4. Deployed on EC2 using Docker

## Environments
- dev
- stage
- prod

## Deployment
Triggered automatically via Jenkins pipeline
