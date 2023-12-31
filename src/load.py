from os import getenv
from dotenv import find_dotenv, load_dotenv
import boto3
from xml.dom.minidom import parse, parseString

load_dotenv(find_dotenv())
S3_ENDPOINT = getenv('S3_ENDPOINT')
S3_BUCKET = getenv('S3_BUCKET')
S3_REGION = getenv('S3_REGION')
S3_ACCESS_KEY = getenv('S3_ACCESS_KEY')
S3_SECRET_ACCESS_KEY = getenv('S3_SECRET_ACCESS_KEY')

S3_OBJECT_EXPORT_INDEX = getenv('S3_OBJECT_EXPORT_INDEX')
S3_OBJECT_EXPORT_INDEX_NAME = getenv('S3_OBJECT_EXPORT_INDEX_NAME')

def s3client():
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_ACCESS_KEY,
        endpoint_url='https://sos-'+S3_REGION+'.'+S3_ENDPOINT,
    )
    return s3_client
    
def uploadFile(filename, bucket, objectname):
    s3 = s3client()
    s3.upload_file(filename, bucket, objectname, ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/xml'})
    
def load(data):
    uploadFile(S3_OBJECT_EXPORT_INDEX_NAME, S3_BUCKET, S3_OBJECT_EXPORT_INDEX)
    return data
