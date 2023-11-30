class Pagination:
    @classmethod
    def create_pagination(
            cls,
            current_page: int,
            total_pages: int,
            boundaries: int,
            around: int
    ) -> None:
        first_boundary = cls.boundary_generator(1, boundaries)
        last_boundary = cls.boundary_generator(total_pages - boundaries + 1, total_pages)

        before_current_page = max(current_page - around, boundaries + 1)
        after_current_page = min(current_page + around, total_pages - boundaries)
        around_current_page = cls.boundary_generator(before_current_page, after_current_page)

        pagination = first_boundary
        pagination += ["..."] * (before_current_page > boundaries + 1)
        pagination += around_current_page
        pagination += ["..."] * (after_current_page < total_pages - boundaries)
        pagination += last_boundary

        print(" ".join(map(str, pagination)))

    @staticmethod
    def boundary_generator(start: int, end: int) -> list:
        return list(range(start, end + 1))
