
let searchForm = document.getElementById('search');
let pagelinks = document.querySelectorAll('.page-link');

if (searchForm) {
    for (let i = 0; i < pagelinks.length; i++) {
        pagelinks[i].addEventListener('click', function(e) {
            e.preventDefault();
            let page = this.dataset.page;
            searchForm.innerHTML += `<input type='hidden' name='page' value='${page}'>`;
            searchForm.submit();
        });
    }
}