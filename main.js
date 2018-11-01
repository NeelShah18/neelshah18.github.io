$(function () {
    $("#home").on('click', function (e) {
        $("#home").addClass('active');

        $("#aboutme").removeClass('active');
        $("#thoughts").removeClass('active');
        $("#friends").removeClass('active');
        $("#contact").removeClass('active');

        hideAllContainers();
        $('#homeContent').show();
    });

    $("#thoughts").on('click', function (e) {
        $("#thoughts").addClass('active');

        $("#aboutme").removeClass('active');
        $("#home").removeClass('active');
        $("#friends").removeClass('active');
        $("#contact").removeClass('active');

        hideAllContainers();
        $('#thoughtsContent').show();
    });

    $("#aboutme").on('click', function (e) {
        $("#aboutme").addClass('active');

        $("#thoughts").removeClass('active');
        $("#home").removeClass('active');
        $("#friends").removeClass('active');
        $("#contact").removeClass('active');

        hideAllContainers();
        $('#aboutmeContent').show();
    });

    $("#friends").on('click', function (e) {
        $("friends").addClass('active');

        $("#home").removeClass('active');
        $("#thoughts").removeClass('active');
        $("#contact").removeClass('active');
        $("#aboutme").removeClass('active');

        hideAllContainers();
        $('#friendsContent').show();
    });

    $("#contact").on('click', function (e) {
        $("#contact").addClass('active');

        $("#home").removeClass('active');
        $("#aboutme").removeClass('active');
        $("#thoughts").removeClass('active');
        $("#friends").removeClass('active');

        hideAllContainers();
        $('#contactContent').show();
    });
});

function hideAllContainers() {
    $('.pageContainerCommon').hide();
}
