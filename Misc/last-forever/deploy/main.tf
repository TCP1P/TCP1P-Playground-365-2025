terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  profile = "awscli"
  region  = "us-east-2"
  shared_credentials_files = ["/home/curiozan/.aws/credentials"]
}

# S3 Bucket name

resource "aws_s3_bucket" "my_s3_bucket" {
  bucket = "forever.lychnobyte.my.id"
}

# Active Versioning

resource "aws_s3_bucket_versioning" "my_s3_bucket_versioning" {
  bucket = aws_s3_bucket.my_s3_bucket.bucket
  versioning_configuration {
    status = "Enabled"
  }
}

# ACL and access configuration

resource "aws_s3_bucket_acl" "bucket-acl" {
  bucket = aws_s3_bucket.my_s3_bucket.id
  acl    = "public-read"
  depends_on = [aws_s3_bucket_ownership_controls.s3_bucket_acl_ownership]
}

resource "aws_s3_bucket_ownership_controls" "s3_bucket_acl_ownership" {
  bucket = aws_s3_bucket.my_s3_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
  depends_on = [aws_s3_bucket_public_access_block.public_access_block]
}

resource "aws_s3_bucket_public_access_block" "public_access_block" {
  bucket = aws_s3_bucket.my_s3_bucket.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}


resource "aws_s3_bucket_policy" "bucket-policy" {
  bucket = aws_s3_bucket.my_s3_bucket.id
  policy = data.aws_iam_policy_document.s3-iam-policy.json
}

data "aws_iam_policy_document" "s3-iam-policy" {
  statement {
    sid    = "AllowPublicRead"
    effect = "Allow"
resources = [
      "arn:aws:s3:::forever.lychnobyte.my.id/*",
    ]
actions = ["S3:GetObject"]

principals {
      type        = "*"
      identifiers = ["*"]
    }
  }

  depends_on = [aws_s3_bucket_public_access_block.public_access_block]
}

# Website Config file

resource "aws_s3_bucket_website_configuration" "my_website_config" {
  bucket = aws_s3_bucket.my_s3_bucket.id
  index_document {
    suffix = "index.html"
  }
  error_document {
    key = "404.html"
  }
}

# Upload file

resource "aws_s3_object" "upload_html_object" {
  for_each      = fileset("../sites/", "*.html")
  bucket        = aws_s3_bucket.my_s3_bucket.id
  key           = each.value
  source        = "../sites/${each.value}"
  etag          = filemd5("../sites/${each.value}")
  content_type  = "text/html"
  acl           = "public-read"
}

resource "aws_s3_object" "upload_txt_object" {
  for_each      = fileset("../sites/", "*.txt")
  bucket        = aws_s3_bucket.my_s3_bucket.id
  key           = each.value
  source        = "../sites/${each.value}"
  etag          = filemd5("../sites/${each.value}")
  content_type  = "text/html"
  acl           = "public-read"
}

resource "aws_s3_object" "upload_png_object" {
  for_each      = fileset("../sites/", "*.png")
  bucket        = aws_s3_bucket.my_s3_bucket.id
  key           = each.value
  source        = "../sites/${each.value}"
  etag          = filemd5("../sites/${each.value}")
  content_type  = "image/png"
  acl           = "public-read"
}

resource "aws_s3_object" "upload_mp3_object" {
  for_each      = fileset("../sites/", "*.mp3")
  bucket        = aws_s3_bucket.my_s3_bucket.id
  key           = each.value
  source        = "../sites/${each.value}"
  etag          = filemd5("../sites/${each.value}")
  content_type  = "audio/mpeg"
  acl           = "public-read"
}