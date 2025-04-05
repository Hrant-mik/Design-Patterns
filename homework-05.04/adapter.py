class OldSystem:
    def legacy_operation(self):
        return "Legacy operation"

class Adapter(OldSystem):
    def new_operation(self):
        return f"Adapter: {self.legacy_operation()}"

def client_code(adapter):
    result = adapter.new_operation()
    print(result)

if __name__ == "__main__":
    adapter = Adapter()
    client_code(adapter)