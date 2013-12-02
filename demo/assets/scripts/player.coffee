$ ->
    data = new Array()
    checkTimer = null

    get_json_data = () ->
        $.ajax {
                url: '/getdata',
                dataType: 'json',
                success: (items) ->
                    data = items
                    return;
            }
        return ;

    check_duration = () ->
        obj = document.getElementById('player')
        currentTime = obj.currentTime
        for item in data
            if (Math.abs(currentTime - item.time) < 0.5)
                $("#player-mask").height($("#player-container").height())
                $("#player-mask").width($("#player-container").width())
                $("#player-mask > .quetion").html(item.q)
                $("#player-mask > .opts").html(item.a)
                $("#player-mask").show()
                clearInterval(checkTimer)
                obj.pause()
        return ;

    $("#continue-btn").click ->
        obj = document.getElementById('player')
        $("#player-mask").hide()
        checkTimer = setInterval(check_duration, 1000)
        obj.play()

    $("#player-mask").hide()
    get_json_data()
    checkTimer = setInterval(check_duration, 1000)
    return ;
 