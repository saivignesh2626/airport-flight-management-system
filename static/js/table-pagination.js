document.addEventListener("DOMContentLoaded", function () {
    const ROWS_PER_PAGE = 5;

    document.querySelectorAll("table").forEach(function (table) {
        // Collect ONLY rows that have <td> elements (skips header rows with <th>)
        const rows = Array.from(table.querySelectorAll("tr")).filter(function (tr) {
            return tr.querySelector("td") !== null;
        });

        const totalRows = rows.length;

        // Wrap the table in .table-container if not already wrapped
        if (!table.parentElement.classList.contains("table-container")) {
            const container = document.createElement("div");
            container.className = "table-container";
            table.parentNode.insertBefore(container, table);
            container.appendChild(table);
        }

        // If 5 or fewer actual data rows, don't paginate
        if (totalRows <= ROWS_PER_PAGE) return;

        let currentPage = 1;
        const totalPages = Math.ceil(totalRows / ROWS_PER_PAGE);

        const nav = document.createElement("div");
        nav.className = "pagination-controls";
        nav.innerHTML = `
            <span class="page-info">Showing page ${currentPage} of ${totalPages} (${totalRows} total records)</span>
            <div class="pagination-buttons">
                <button type="button" class="page-btn btn-prev">Previous</button>
                <button type="button" class="page-btn btn-next">Next</button>
            </div>
        `;

        const targetContainer = table.closest(".table-container");
        targetContainer.parentNode.insertBefore(nav, targetContainer.nextSibling);

        const prevBtn = nav.querySelector(".btn-prev");
        const nextBtn = nav.querySelector(".btn-next");
        const pageInfo = nav.querySelector(".page-info");

        function renderPage(page) {
            const start = (page - 1) * ROWS_PER_PAGE;
            const end = start + ROWS_PER_PAGE;

            // Only show/hide data rows; the header remains untouched
            rows.forEach((row, index) => {
                row.style.display = index >= start && index < end ? "" : "none";
            });

            pageInfo.textContent = `Showing page ${page} of ${totalPages} (${totalRows} total records)`;
            prevBtn.disabled = page === 1;
            nextBtn.disabled = page === totalPages;
        }

        prevBtn.addEventListener("click", function () {
            if (currentPage > 1) {
                currentPage--;
                renderPage(currentPage);
            }
        });

        nextBtn.addEventListener("click", function () {
            if (currentPage < totalPages) {
                currentPage++;
                renderPage(currentPage);
            }
        });

        renderPage(1);
    });
});