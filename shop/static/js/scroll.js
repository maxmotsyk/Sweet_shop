$("a[href='#cake']", "a[href='#chesse_cake']", "a[href='#marshmellow']", "a[href='#cap_cake']").click(function() {
    $("html, body").animate({ scrollBottom: 0 }, "slow");
    return false;
  });

