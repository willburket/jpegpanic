

$.ajax({
    type: 'GET',
    url: '/articles-json/',
    success: function(response){
        console.log(response)
    },
    error: function(error){
        console.log(error)
    }
})
