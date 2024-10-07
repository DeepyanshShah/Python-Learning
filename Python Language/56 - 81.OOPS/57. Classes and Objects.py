class God:
    name = "Thor"
    title = "Thunder-God"
    networth = 9999

    def info(self):
        print(f"{self.name} is a {self.title}")

a = God()
a.name = "Kratos"
a.title = "God-of-War"
a.info()

b = God()
b.name = "Odin"
b.title = "All-father"
b.info()