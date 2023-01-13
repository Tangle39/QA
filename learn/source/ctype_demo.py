import ctypes


class UniqueLittleEndianStructure(ctypes.LittleEndianStructure):
    def as_dict(self):
        """
        @brief: translate struct to a dict, this at most deal with 2-dimension array
        :return: a dict
        """
        res = {}
        for field in self.fields:
            value = getattr(self, field)
            if hasattr(value, '_length_') and hasattr(value, '_type_'):
                value = list(value)
                if hasattr(value[0], '_length_') and hasattr(value[0], '_type_'):
                    for idx, tmp_val in enumerate(value):
                        value[idx] = list(tmp_val)
            elif hasattr(value, '_fields_'):
                value = value.as_dict()
            res[field] = value

        return res

    @property
    def fields(self):
        """@brief: get fields"""
        tmp = []
        for field, _ in self._fields_:
            tmp.append(field)
        return tmp

    def __setattr__(self, key, value):
        """
        @brief: set value for class
        """
        if isinstance(value, list):
            super().__setattr__(key, (type(getattr(self, key))(*value)))
        else:
            super().__setattr__(key, value)


class Unel(UniqueLittleEndianStructure):
    class SubUnel(UniqueLittleEndianStructure):
        _pack_ = 1
        _fields_ = [
            ('rd_level', ctypes.c_int8 * 2),
            ('err_type', ctypes.c_uint8 * 3 * 4)
        ]

    _pack_ = 1
    _fields_ = [
        ('poh', ctypes.c_uint16 * 3),
        ('ch', ctypes.c_uint8),
        ('lun', ctypes.c_uint8 * 2 * 3),
        ('key', SubUnel)
    ]


if __name__ == '__main__':
    b = Unel()
    value1 = [1, 2, 3]
    b.__setattr__('poh', value1)
    setattr(b, 'ch', 5)
    print(b.as_dict())
