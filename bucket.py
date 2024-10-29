from google.cloud import storage
 
client = storage.Client()
 
for b in client.list_buckets():
    print("Bucket name: %s " % b.name)
    for o in client.list_blobs(b.name):
        print("Object name: %s" % o.name)

#source cloud-env/bin/activate