from libqtile.config import Group


def init_groups():
    groups = [
        Group("󰀘 ", layout="monadtall"),
        Group("󰃭 ", layout="monadtall"),
        Group(" ", layout="monadtall"),
        Group(" ", layout="monadtall"),
        Group(" ", layout="monadtall"),
        Group("󰈰", layout="monadtall"),
        Group("󰎈", layout="monadtall"),
        Group("󰙊 ", layout="floating"),
    ]
    return groups
