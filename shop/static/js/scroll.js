$("a[href='#cake']", "a[href='#chessecake']", "a[href='#marshmellow']", "a[href='#capcake']").click(function() {
    $("html, body").animate({ scrollBottom: 0 }, "slow");
    return false;
  });

