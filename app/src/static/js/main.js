// Bootstrap toasts
let toasts = [].slice.call(document.getElementsByClassName('toast'))

if (toasts) {
    for (let el in toasts) {
        if (el !== 'length') {
            let toast = new bootstrap.Toast(toasts[el])
            toast.show()
        }
    }
}
