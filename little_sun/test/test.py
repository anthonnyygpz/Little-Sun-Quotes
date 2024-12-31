import reflex as rx


class State(rx.State):
    allTags: list[str] = ["tag1", "tag2", "tag3"]
    isTagChecked: dict[str, bool] = {k: False for k in allTags}

    def toggleTagChecked(self, tag):
        checked = self.isTagChecked.copy()
        checked[tag] = not checked[tag]
        self.isTagChecked = checked
        print(self.isTagChecked)

    def uncheck_all(self):
        # Crear una copia nueva del diccionario con todos los valores en False
        self.isTagChecked = {k: False for k in self.allTags}


def tagView(tagText):
    return rx.hstack(
        rx.checkbox(
            tagText,
            checked=State.isTagChecked[tagText],
            on_click=lambda: State.toggleTagChecked(tagText),
        ),
    )


def test():
    return rx.vstack(
        rx.foreach(
            State.allTags,
            lambda item: tagView(item),
        ),
        rx.button("Desmarcar Todos", on_click=State.uncheck_all),
    )
