# YouTube-Thumbnail-Stats-Updater

---

YT Thumbnail Stats is a Python script that allows you to dynamically update YouTube video thumbnails with real-time view counts. This enhances the visual appeal of your videos on YouTube and provides viewers with valuable information about the popularity of your content.

## Features

- **Dynamic Thumbnail Updates**: Automatically update YouTube video thumbnails with the latest view counts.
- **Customizable**: Modify the script to include additional information or customize the appearance of the thumbnails.
- **Easy to Use**: Simple setup process with detailed instructions provided.

## How it Works

1. **Setup Credentials**: Obtain credentials for accessing the YouTube Data API and save them in a JSON file.
2. **Install Dependencies**: Ensure you have the necessary Python libraries installed, including `google-auth-oauthlib`, `google-auth`, `google-api-python-client`, and `Pillow`.
3. **Configure Script**: Update the script with your video ID, thumbnail path, and credentials file path.
4. **Run the Script**: Execute the Python script to retrieve the latest view count for your video, overlay it on the thumbnail image, and upload the updated thumbnail to YouTube.

## Prerequisites

Before using this script, you'll need:

- Python 3 installed on your system.
- Client credentials for the YouTube Data API stored in a JSON file.

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python libraries using pip:

```
pip install -r requirements.txt
```

3. Follow the setup instructions in the script to obtain your client credentials and update the configuration variables.

## Usage

To use the script:

1. Ensure your video ID, thumbnail path, and credentials file path are correctly configured in the script.
2. Run the script using the following command:

```
python main.py
```

3. The script will retrieve the latest view count for your video, overlay it on the thumbnail image, and upload the updated thumbnail to YouTube.


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to suggest improvements or additional features.

## Support

If you encounter any issues or have questions about using the script, please [open an issue](https://github.com/PriyanshRaj30/yt-thumbnail-stats/issues) on GitHub.

---

