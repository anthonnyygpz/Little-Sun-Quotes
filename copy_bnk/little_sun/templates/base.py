import reflex as rx


def create_stylesheet_link(stylesheet_url):
    """Create a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def base_template(content):
    """Base template for all pages."""
    return rx.fragment(
        create_stylesheet_link(
            stylesheet_url="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
        ),
        create_stylesheet_link(
            stylesheet_url="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
        ),
        rx.el.style(
            """
            @font-face {
                font-family: 'LucideIcons';
                src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
            }
            """
        ),
        rx.box(
            content,
            class_name="font-[Poppins]",
            background_color="#F3F4F6",
        ),
    )
