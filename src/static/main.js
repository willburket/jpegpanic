
let visible = 6

const articlesBox = document.getElementById('articles-box')
const spinnerBox = document.getElementById('spinner-box')


const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `/articles-json/${visible}`,
        success: function(response){
            // console.log(response.data)
            const data = response.data
            data.map(post=>{
                console.log(post.id)
            })
        },
        error: function(error){
            console.log(error)
        }
    })

}

handleGetData()


window.onload = function(){
    const loadBtn = document.getElementById('load-btn')
    loadBtn.addEventListener('click', ()=>{
        visible += 3
        handleGetData()
    })
}


