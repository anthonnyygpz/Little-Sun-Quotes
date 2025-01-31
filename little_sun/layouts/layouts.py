import reflex as rx

from little_sun.sections.header.navbar import navbar


def create_stylesheet_link(stylesheet_url):
    """Create a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")


def layout(content):
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
            rx.box(
                navbar(),  # Call the navbar function to render it
                height="8em",
            ),
            content,  # Place your content after the navbar.
            class_name="font-[Poppins]",
            width="100%",
            spacing="6",
            padding_x=["1.5em", "1.5em", "3em"],
        ),
    )

