from pydantic import BaseModel


class DTOBaseModel(BaseModel):
    @classmethod
    def dto_parse(cls, obj=None, **kwargs):
        """
        obj:
          - ORM 객체
          - dict
          - None
        kwargs:
          - 커스텀 필드 조합
        """
        if obj is not None:
            # ORM 객체면 from_attributes=True로 처리
            try:
                base_dict = cls.model_validate(obj, from_attributes=True).model_dump()
            except Exception:
                # dict라면 그대로 사용 가능
                if isinstance(obj, dict):
                    base_dict = obj
                else:
                    raise
        else:
            base_dict = {}

        # obj에서 가져온 값 + kwargs override
        final_data = {**base_dict, **kwargs}
        return cls(**final_data)
