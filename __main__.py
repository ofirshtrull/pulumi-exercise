"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3
import settings

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket(
    '{}-pulumi-bucket'.format(settings.PROJECT_NAME),
    )

bucket_object = s3.BucketObject(
    'index.html',
    bucket=bucket,
    source=pulumi.FileAsset('assets/index.html')
    )


# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
pulumi.export('bucket_endpoint', bucket.bucket_regional_domain_name)
pulumi.export('project_name', settings.PROJECT_NAME)
