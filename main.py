class Pagination:
    @staticmethod
    def create_pagination(
        current_page: int, total_pages: int, boundaries: int, around: int
    ) -> None:
        first_boundary = Pagination._generate_first_boundary_or_print_result(
            boundaries, total_pages
        )
        if first_boundary is None:
            return

        last_boundary = Pagination._generate_last_boundary_or_print_result(
            first_boundary, boundaries, total_pages
        )
        if last_boundary is None:
            return

        before_current_page = max(current_page - around, boundaries + 1)
        after_current_page = min(current_page + around, total_pages - boundaries)
        around_current_page = Pagination.boundary_generator(
            before_current_page, after_current_page
        )

        pagination = first_boundary
        pagination += ["..."] if before_current_page > boundaries + 1 else ""

        pagination += around_current_page
        pagination += ["..."] if after_current_page < total_pages - boundaries else ""

        pagination += last_boundary

        print(" ".join(map(str, pagination)))

    @staticmethod
    def _generate_first_boundary_or_print_result(
        boundaries: int, total_pages: int
    ) -> list | None:
        if boundaries > total_pages:
            result = Pagination.boundary_generator(1, total_pages)
            print(" ".join(map(str, result)))
            return
        else:
            return Pagination.boundary_generator(1, boundaries)

    @staticmethod
    def _generate_last_boundary_or_print_result(
        first_boundary: list, boundaries: int, total_pages: int
    ) -> list | None:
        if boundaries > total_pages / 2:
            last_boundary = Pagination.boundary_generator(boundaries + 1, total_pages)
            print(" ".join(map(str, first_boundary + last_boundary)))
            return
        else:
            return Pagination.boundary_generator(
                total_pages - boundaries + 1, total_pages
            )

    @staticmethod
    def boundary_generator(start: int, end: int) -> list:
        return list(range(start, end + 1))
