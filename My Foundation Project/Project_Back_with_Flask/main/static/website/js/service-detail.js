// Acc
$(document).on("click", ".service-detail .menu div", function() {
	var numberIndex = $(this).index();

	if (!$(this).is("active")) {
		$(".service-detail .menu div").removeClass("active");
		$(".service-detail ul li").removeClass("active");

		$(this).addClass("active");
		$(".service-detail ul").find("li:eq(" + numberIndex + ")").addClass("active");

		var listItemHeight = $(".service-detail ul")
			.find("li:eq(" + numberIndex + ")")
			.innerHeight();
		$(".service-detail ul").height(listItemHeight + "px");
	}
});
