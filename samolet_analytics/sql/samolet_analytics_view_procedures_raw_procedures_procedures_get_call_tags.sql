### `agg_procedures.get_call_tags`(call_tags) as call_tags,
  ARRAY_TO_STRING(REGEXP_EXTRACT_ALL(call_tags, r'"names":\[(.+?)\]'),',')