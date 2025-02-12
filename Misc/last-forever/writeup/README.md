# Writeup Last Forever

### Main idea
Static website run on top AWS s3 bucket with versioning enabled

### How
List all available version of file `myheart.txt`, retrieve all data from each version. Then combined to become valid flag.

### Example
1. Access to http://forever.lychnobyte.my.id.s3.amazonaws.com/?versions
2. Create some script to looping read each version

### Reference
1. https://docs.aws.amazon.com/AmazonS3/latest/userguide/list-obj-version-enabled-bucket.html
2. https://docs.aws.amazon.com/id_id/AmazonS3/latest/userguide/RetrievingObjectVersions.html