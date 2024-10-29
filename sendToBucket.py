from google.cloud import storage
bucket_name = "pwzal-bucket"
print("Podaj nazwe zdięcia: ")
fileName = input()
print("Podaj kat obrotu: ")
angle = int(input())
client = storage.Client()
bucket = client.bucket(bucket_name)

blob = bucket.blob(fileName)
generation_match_precondition = 0
metageneration_match_precondition = None

blob.upload_from_filename(fileName, if_generation_match=generation_match_precondition)
print(f"File {fileName} uploaded to blob")

metageneration_match_precondition = blob.metageneration
metadata = {'angle': angle}
blob.metadata = metadata
blob.patch(if_metageneration_match=metageneration_match_precondition)
print(f"The metadata for the blob {blob.name} is {blob.metadata}")