import reflex as rx


def create_label(label_text):
    """Create a label element with specific styling."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="500",
        margin_bottom="0.25rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


# def create_checkbox_label(label_text):
#     """Create a label for a checkbox with specific styling."""
#     return rx.el.label(
#         label_text,
#         display="block",
#         margin_left="0.5rem",
#         color="#111827",
#         font_size="0.875rem",
#         line_height="1.25rem",
#     )
#

def create_heading(text):
    """Create a heading element with specific styling."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h2",
    )