$(document).ready(function(){

    $('#perf-row').hide()
  
    $('#show-perf').click(function(){
    $('#perf-row').slideToggle(200)
    });

    $('#numbering-row').hide()
  
    $('#show-numbering').click(function(){
    $('#numbering-row').slideToggle(200)
    });

    $('#wrap-row').hide()

    $('#show-wraparound').click(function(){
    $('#wrap-row').slideToggle(200)
    });

    $('#mailmerge-row').hide()

    $('#show-mailmerge').click(function(){
    $('#mailmerge-row').slideToggle(200)
    });

    $('#padding-row').hide()

    $('#show-padding').click(function(){
    $('#padding-row').slideToggle(200)
    });

    $('#drill-row').hide()

    $('#show-drill').click(function(){
    $('#drill-row').slideToggle(200)
    });

    $('#staple-row').hide()

    $('#show-staple').click(function(){
    $('#staple-row').slideToggle(200)
    });

    $('#fold-row').hide()

    $('#show-fold').click(function(){
    $('#fold-row').slideToggle(200)
    });

    $('#tab-row').hide()

    $('#show-tab').click(function(){
    $('#tab-row').slideToggle(200)
    });

    $('#bulkmail-row').hide()

    $('#show-bulkmail').click(function(){
    $('#bulkmail-row').slideToggle(200)
    });






    //Autofill qtys on newjob form
    $('#id_set_per_book, #id_pages_per_book, #id_qty_of_sheets, #id_overage, #id_press_size_per_parent, #id_gangup, #id_step_print_cost_side_1, #id_step_print_cost_side_2').change(function(){
      //alert( "Handler for `keyup` called." );
      var set_per_book = $('#id_set_per_book').val();
      var pages_per_book = $('#id_pages_per_book').val();
      var overage = $('#id_overage').val();
  
      var press_size_per_parent = $('#id_press_size_per_parent').val();
      var gangup = $('#id_gangup').val();


      
      var set_per_book = Number(set_per_book);
      var pages_per_book = Number(pages_per_book);
      var overage = Number(overage);
      var press_size_per_parent = Number(press_size_per_parent);
      var gangup = Number(gangup);
      
      
      var sheet_qty = set_per_book * pages_per_book;
      
      var output = press_size_per_parent * gangup;
      
      var c = sheet_qty + overage;
      var parent = c / output;
      var parent = Math.ceil(parent);
  
      var click1 = press_size_per_parent * parent
      var click2 = press_size_per_parent * parent


      
  
      $('#id_qty_of_sheets').val(sheet_qty);
  
      $('#id_output_per_sheet').val(output);
      
      $('#id_parent_sheets_required').val(parent);
  
      $('#id_side_1_clicks').val(click1);
      $('#id_side_2_clicks').val(click2);

      

      //Calculate printing cost. Number of clicks * price / click rounded to two decimals
      var printcost1 = $('#id_step_print_cost_side_1').val();
      var printcost2 = $('#id_step_print_cost_side_2').val();

      var printcost1 = Number(printcost1);
      var printcost2 = Number(printcost2);
      
      var clickcost1 = click1 * printcost1
      var clickcost2 = click2 * printcost2

      clickcost1 = clickcost1.toFixed(2);
      clickcost2 = clickcost2.toFixed(2);

      $('#id_step_print_cost_side_1_price').val(clickcost1);
      $('#id_step_print_cost_side_2_price').val(clickcost2);

      $('#id_mailmerge_qty').val(sheet_qty)
      $('#id_perf_number_of_pieces').val(sheet_qty)
      $('#id_perf_number_of_pieces').val(sheet_qty)
      $('#id_number_number_of_pieces').val(sheet_qty)
      //Insert number to drill after it gets added to form
      $('#id_staple_number_of_pieces').val(set_per_book)
      $('#id_tabs_number_of_pieces').val(set_per_book)
      
  
    });
  
    
  
    $('#id_press_size_per_parent, #id_gangup, #id_output_per_sheet').keyup(function(){
      //alert( "Handler for `keyup` called." );
      var press_size_per_parent = $('#id_press_size_per_parent').val();
      var gangup = $('#id_gangup').val();
      var output = press_size_per_parent * gangup
  
      $('#id_output_per_sheet').val(output);
  
  
    });


    $('#id_mailmerge_qty, #id_mailmerge_price_per_piece').keyup(function(){
      //alert( "Handler for `keyup` called." );
      var mailmerge = $('#id_mailmerge_qty').val();
      var price = $('#id_mailmerge_price_per_piece').val();

      //var mailmerge = Number(mailmerge);
      //var price = Number(price);

      var mailmerge_price = mailmerge * price
      mailmerge_price = mailmerge_price.toFixed(2);

      $('#id_step_print_mailmerge_price').val(mailmerge_price);
  
  
    });
  

  
  
  
  });