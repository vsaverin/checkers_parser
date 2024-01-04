import json


class LogsService:
    def generate_string_output(self, values: list[dict]) -> list[str]:
        formatted = []
        for item in values:
            data = ""
            data += f'\nType: {item.get("type")}'
            data += f'\nRank: {item.get("rank")}'
            data += f'\nLine No.: {item.get("lineno")}'
            data += f'\nEndline: {item.get("endline")}'
            data += f'\nName: {item.get("name")}'
            data += f'\nComplexity: {item.get("complexity")}'
            data += f'\nClass name: {item.get("classname")}'
            formatted.append(data)
        return formatted

    def get_radon_formatted_data(self, absolute_path: str):
        response = []
        with open(absolute_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for k, v in data.items():
                formatted_values = self.generate_string_output(v)
                for value in formatted_values:
                    response.append({"in_file": k, "value": value})
        return response

    def mi_generate_string_output(self, value: dict) -> str:
        data = ""
        data += f'\nMaintainability Index: {value.get("mi")}'
        data += f'\nRank: {value.get("rank")}'
        return data

    def mi_get_radon_formatted_data(self, absolute_path: str):
        response = []
        with open(absolute_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for k, v in data.items():
                print(k, v)
                formatted_values = self.mi_generate_string_output(v)
                response.append({"in_file": k, "value": formatted_values})
        return response

    def ruff_generate_string_output(self, report: dict) -> str:
        response = ""
        for key, value in report.items():
            if key == "filename":
                continue
            response += f"\n{key}: {value}"
        return response

    def get_ruff_formatted_data(self, absolute_path: str):
        response = []
        with open(absolute_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for report in data:
                formatted_values = self.ruff_generate_string_output(report)
                response.append(
                    {"in_file": report.get("filename"), "value": formatted_values}
                )
        return response

    def bandit_generate_string_output(self, value: dict) -> dict:
        code = f"\nCode:\n{value.pop('code')}"
        response = ""
        for k, v in value.items():
            response += f"\n{k}: {v}"
        return {"value": response, "code": code}

    def get_bandit_formatted_data(self, absolute_path: str):
        response = []
        with open(absolute_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data.get("results"):
                filename = item.pop("filename")
                formatted_values = self.bandit_generate_string_output(item)
                if not formatted_values:
                    continue
                response.append(
                    {
                        "in_file": filename,
                        "code": formatted_values.get("code"),
                        "value": formatted_values.get("value"),
                    }
                )
        return response
