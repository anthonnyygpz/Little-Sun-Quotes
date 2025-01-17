import reflex as rx


def _badge(icon: str, text: str, color_scheme: str):
    return rx.badge(
        rx.icon(icon, size=16),
        text,
        color_scheme=color_scheme,
        radius="full",
        variant="soft",
        size="3",
    )


def status_badge(status: str):
    badge_mapping = {
        "Completed": ("check", "Completado", "green"),
        "Pending": ("loader", "Pendiente", "yellow"),
        "Cancelled": ("ban", "Cancelado", "red"),
    }
    return _badge(*badge_mapping.get(status, ("loader", "Pending", "yellow")))
