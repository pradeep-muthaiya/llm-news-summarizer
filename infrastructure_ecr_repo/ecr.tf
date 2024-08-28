resource "aws_ecr_repository" "ecr_test_repo" {
  name                 = "ecr_news_repository"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}