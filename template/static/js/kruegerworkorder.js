$(document).ready(function(){
    //Autofill qtys on newjob form
    $('#id_set_per_book, #id_pages_per_book, #id_qty_of_sheets, #id_overage, #id_press_size_per_parent, #id_gangup').keyup(function(){
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
  
    });
  
    
  
    $('#id_press_size_per_parent, #id_gangup, #id_output_per_sheet').keyup(function(){
      //alert( "Handler for `keyup` called." );
      var press_size_per_parent = $('#id_press_size_per_parent').val();
      var gangup = $('#id_gangup').val();
      var output = press_size_per_parent * gangup
  
      $('#id_output_per_sheet').val(output);
  
  
    });
  

  
  
  
  });
  