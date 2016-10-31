class Line:
  def __init__(self, fields):
    self.fields = fields

  def merge(self):
    merged_fields = []
    empty_fields = []

    for (index, field) in enumerate(self.fields):
      if(field == 0):
        empty_fields.append(field)
        continue

      previous_field = self.fields[index-1] if index > 0 else None

      if(previous_field == field):
        merged_fields[len(merged_fields) - 1] = field + previous_field
        self.fields[index] = 0
        empty_fields.append(0)
        continue

      merged_fields.append(field)

    merged_fields.extend(empty_fields)

    self.fields = merged_fields
