    var index = 0;
    var res = [];
    var mailList = [];

    function myFunction(objValue){

        e = document.getElementById("id_send");
        mail = document.getElementById("mailList");

        for(i = 0; i <= index; i++){
             if (("+ "+objValue.id + "\n") == res[i]){
                objValue.style.background = "#dfe3ee";
                objValue.innerHTML = "hinzufügen";
                objValue.style.color = "black";
                mailList.splice(i, 1);
                res.splice(i, 1);
                e.innerHTML = res;
                mail.innerHTML = mailList;
                index--;
                console.log(objValue.id);
                return
            }
        }

        if (index == 5){
            alert("Eine Anfrage - 5 Firmen maximal!")
        }

        if (index < 5){
            objValue.style.background = "#00468C";
            objValue.style.color = "white";
            objValue.innerHTML = "von der Liste löschen";

            {% for firm in firma_new %}
                if ("{{ firm.name }}" == objValue.id) {
                    res[index] = "+ "+objValue.id + "\n";
                    mailList[index] = " " + objValue.value;
                    mail.innerHTML = mailList;
                    e.innerHTML = res;
                    index++;
                }
            {% endfor %}
        }

    }

    //resize the screen
     window.addEventListener('resize', Wchange);
     function Wchange(){
        var width = window.outerWidth;

        if(width > 760){
            $('#form-back').css('height', '2400px');

        }else{
            $('#form-back').css('height', '100%');
            $('#aform').css('position','static');
        }
     }

    //scroll to top function
    $(document).ready(function () {

        elementPosition = $('#aform').offset();
        mapPosition = $('#sample').offset();

        $(window).scroll(function () {

            if ($(this).scrollTop() > 350) {
                $('#back-to-top').fadeIn();
                $('#search_bar2').fadeIn();
            } else {
                $('#back-to-top').fadeOut();
                $('#search_bar2').fadeOut();
            }

            //fluid form
            if($(window).width() < 760){
                $('#form-back').css('height', '100%');
            }else{
                if($(window).scrollTop() > elementPosition.top-150){

                    $('#aform').addClass('col-md-3 col-sm-4').css('position','fixed').css('top','100px').css('bottom','');

                    if($(window).scrollTop() > mapPosition.top-950){
                        $('#aform').css('position','absolute').css('bottom','0').css('top','');
                        $('#aform').removeClass('col-md-3 col-sm-4')
                    }
                }
                else{
                    $('#aform').css('position','static');
                    $('#aform').removeClass('col-md-3 col-sm-4')
                }
            }

        });

        // scroll body to 0px on click
        $('#back-to-top').click(function () {
            $('#back-to-top').tooltip('hide');
            $('body,html').animate({
                scrollTop: 0
            }, 800);
            return false;
        });

        $('#back-to-top').tooltip('show');
    });

    $(function () {
        var options = {'style': 'width:200px'};
        $('[data-toggle="popover"]').popover(options)
    });

    $(document).ready(function(){
        $('[data-toggle="tooltip"]').tooltip();
    });
