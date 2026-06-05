import json
import boto3

client  = boto3.client('s3',
    aws_access_key_id='AKIAYUIYKDDWYAHQYDKX',
    aws_secret_access_key='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'
                       )
source_bucket = 'offline12-demo-593293351149-ap-south-1-an'
destination_bucket  = 'ainexusit-online91111'


def copy_to_destination_bucket(fname):
    client.copy_object(Bucket='{}'.format(destination_bucket),CopySource='/{}/{}'.format(source_bucket,fname),Key='{}'.format(fname))


def delete_from_source_bucket(fname):
    response = client.delete_object(Bucket='{}'.format(source_bucket),Key='{}'.format(fname))


def main():
    response = client.list_objects(Bucket='{}'.format(source_bucket))

    for key in response['Contents']:
        filename = key['Key']
        copy_to_destination_bucket(filename)
        delete_from_source_bucket(filename)


if __name__=='__main__':
    main()