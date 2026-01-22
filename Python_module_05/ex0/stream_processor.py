from abc import ABC, abstractmethod
from typing import List, Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list) and
            len(data) > 0 and
            all(isinstance(p, (int, float)) for p in data)
        )

    def process(self, data: List[int]) -> str:
        try:
            forlen = len(data)
            forsum = sum(data)
            avg = forsum / forlen
            return (
                f"Processed {forlen} numeric values"
                f", sum={forsum}, avg={avg}"
            )
        except TypeError:
            return "ERROR ! Invalid numeric data"
        except ZeroDivisionError:
            return "ERROR ! Empty numeric list"

    def format_output(self, result: str) -> str:
        res = super().format_output(result)
        return f"{res}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, str) and
            len(data) > 0
        )

    def process(self, data: str) -> str:
        count = data.split(" ")
        return f"{len(data)} characters, {len(count)} words"

    def format_output(self, result: str) -> str:
        res = super().format_output(result)
        return f"Processing text: {res}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, str) and
            len(data) > 0
        )

    def process(self, data: str) -> str:
        if "ERROR" in data:
            txt = f"[ALERT] ERROR level detected: {data}"
        elif "INFO" in data:
            txt = f"[INFO] INFO level detected: {data}"
        else:
            txt = ("ERROR ! Invalid Log")
        return f"{txt}"

    def format_output(self, result: str) -> str:
        res = super().format_output(result)
        return res


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    num = NumericProcessor()
    data = [10, 20, 30]
    if num.validate(data):
        print("Initializing Numeric Processor...")
        processor = num.process(data)
        print("Processing data:", data)
        print("Validation: Numeric data verified")
        print("Output:", num.format_output(processor))
    print()
    txt = TextProcessor()
    thetxt = "Hello Nexus World"
    if txt.validate(thetxt):
        print("Initializing Text Processor...")
        text = txt.process(thetxt)
        print(f"Processing data: \"{thetxt}\"")
        print("Validation: Text data verified")
        print(f"Output: {txt.format_output(text)}")
    print()
    logtxt = "ERROR: Connection timeout"
    logproc = LogProcessor()
    if logproc.validate(logtxt):
        print("Initializing Log Processor...")
        lp = logproc.process(logtxt)
        print("Processing data:", logtxt)
        print("Validation: Log entry verified")
        print("Output:", logproc.format_output(lp))
        print("\n=== Polymorphic Processing Demo ===\n")
    processors = [
        TextProcessor(),
        NumericProcessor(),
        LogProcessor(),
    ]
    test = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello World!"),
        (LogProcessor(), "INFO: System ready")
    ]
    i = 1
    print("Processing multiple data types through same interface...")
    for proc, data in test:
        if proc.validate(data):
            result = proc.process(data)
            print(f"Result {i}: {proc.format_output(result)}")
            i += 1
