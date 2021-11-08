let searchForm = document.getElementById('searchForm')
let pageLink = document.getElementsByClassName('pageLink')

if (searchForm) {
    for (let i=0; pageLink.length > i; i++) {
       pageLink[i].addEventListener('click', function (e) {
       e.preventDefault()
       let page = this.dataset.page
       console.log('Page: ' + page)
       searchForm.innerHTML += `<input value=${page} name="page" hidden />`
       searchForm.submit()
       })
    }
}