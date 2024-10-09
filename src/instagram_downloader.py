import instaloader

def download_instagram_reel(url):
        L = instaloader.Instaloader()
            post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
                L.download_post(post, target="downloads")
                    return f"downloads/{post.shortcode}.mp4"

