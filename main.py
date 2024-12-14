from app_ioc import AppIoc
from process_link_service import ProcessLinkService


if __name__ == "__main__":
    urls: list[str] = [
        ""
        # Add more Youtube URLs here
    ]
    
    process_link_service = ProcessLinkService()
    
    app_ioc = AppIoc(
        process_link_service,
        urls
    )
    
    app_ioc.download_youtube_videos_and_convert_as_mp3()