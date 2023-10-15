def imageDownload(imageUrl:str, imageName: str, imageFileExtension: str):
    import requests
    # Download Data from URL
    response = requests.get(imageUrl)
    downloadedFileName = (imageName + '.' + imageFileExtension)
    open(downloadedFileName, 'wb').write(response.content)


def multiImageDownload(numOfImgs: int):
    for i in range(numOfImgs):
        imageDownload(
            input('Enter image URL : '),
            input('Name of image : '),
            input('Image extension (no periods) : ')
        )

# multiImageDownload(3)

imageDownload(
    input('Enter image URL : '),
    input('Name of image : '),
    input('Image extension (no periods) : ')
)