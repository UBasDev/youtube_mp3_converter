from constants import OUTPUT_PATH
from process_link_service import ProcessLinkService
import validators

class AppIoc:
    def __init__(self, process_link_service: ProcessLinkService, url_list: list[str]):
        self.__validate_arguments(process_link_service, url_list)
        self.url_list = url_list
        self.process_link_service = process_link_service
        
    def download_youtube_videos_and_convert_as_mp3(self) -> None:
        for url in self.url_list:
            if url is None or url.strip() == "" or validators.url(url) is not True:
                raise ValueError("URL is not valid. Please provide a valid Youtube URL")
            try:
                self.process_link_service.download_youtube_as_mp3(url)
            except Exception as e:
                print(f"Failed to download or convert {url}: {e}")
                
    def __validate_arguments(self, process_link_service: ProcessLinkService, url_list: list[str]) -> None:
        if len(url_list) == 0:
            raise ValueError("URL list is empty. Please add at least 1 valid URL")
        if process_link_service is None:
            raise ValueError("ProcessLinkService is not provided. Please initialize an instance for it")