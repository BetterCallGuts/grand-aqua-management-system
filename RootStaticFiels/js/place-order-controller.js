/*
*   ================================= GLOBAL VARIABLES ============================================================
* */
var tblOrder = null;
var selectedRow = null;

/*
*   ================================= document.ready() /  window.load() ============================================================
* */
$(function () {
    initializeDataTable();
    loadAllCustomers();
    loadAllItems();
    initializeTextFields();
});

/*
*   ================================= EVENT HANDLERS ============================================================
* */
$("#btn-save").click(addItemToOrder);
$("#tbl-orders tbody").on("click", "tr", selectOrder);
$("#tbl-orders tbody").on("click", "td:last-child", deleteOrderDetail);
$("#btn-clear").click(deselectAllOrders);
$("#btn-placeorder").click(placeOrder);
$("#cmb-custId option").click(loadCustomerName);
$("#cmb-code option").click(loadItemDescription());

/*
*   ================================= FUNCTIONS ============================================================
* */
function initializeDataTable(callbackFn) {
    if (tblOrder != null) {
        tblOrder.destroy();
    }

    if (callbackFn != undefined) {
        callbackFn();
        if ($("#tbl-orders tbody tr").length > 0) {
            $("#tbl-orders tfoot").addClass("d-none");
        } else {
            $("#tbl-orders tfoot").removeClass("d-none");
        }
    }

    tblOrder = $("#tbl-orders").DataTable({
        "ordering": false,
        "lengthChange": false,
        "pageLength": 5,
        "responsive": true,
        "autoWidth": false,
        "info": false,
    });

    //to remove built in empty message in data table
    $("#tbl-orders tr .dataTables_empty").remove();
}

function selectOrder() {
    deselectAllOrders();
    $(this).addClass("selected-row");

    selectedRow = $(this);
    $("select #cmb-code").val(selectedRow.find("td:first-child").text());
    $("#txt-desc").val(selectedRow.find("td:nth-child(2)").text());
    $("#txt-qty").val(selectedRow.find("td:nth-child(3)").text());
    $("#txt-price").val(selectedRow.find("td:nth-child(4)").text());
    $("#txt-id").attr("disabled", true);
    $("#txt-date").attr("disabled", true);
    $("#txt-name").attr("disabled", true);
    // $("#txt-desc").attr("disabled",true);
    $("#txt-qtyOnHand").attr("disabled", true);

}

function addItemToOrder() {
    var zbon = $("#zbon").val();
    var product = $("#cmb-code").val();
    var howMany = $("#txt-qtyOnHand").val();
    var t5fed = $("#txt-price").val();

    
    console.log(zbon)
    
    console.log(product)

    console.log(howMany)

    console.log(t5fed)


    

    var newRow = "<tr>\n" +
        "                                        <td id='td-code'>" + zbon + "</td>\n" +
        "                                        <td id='td-description'>" + product + "</td>\n" +
        "                                        <td id='td-qty'>" + howMany + "</td>\n" +
        "                                        <td id='td-price'>" + t5fed + "</td>\n" +
        "                                        <td id='td-total'>" + (howMany - t5fed)+ "</td>\n" +
        "                                        <td class='bin'><i class=\"fas fa-trash\"></i></td>\n" +
        "                                    </tr>";

    initializeDataTable(function () {
        $('#tbl-orders tbody').append(newRow);
        $("#btn-clear").click();
    })
}

function deselectAllOrders() {
    $("#tbl-orders tbody tr").removeClass("selected-row");
    $("#btn-save").text("Save");
    selectedRow = null;
}

function deleteOrderDetail() {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            selectedRow.fadeOut(500, function () {
                initializeDataTable(function () {
                    selectedRow.remove();
                    $("#btn-clear").click();
                    Swal.fire(
                        'Deleted!',
                        'Your file has been deleted.',
                        'success'
                    )
                });
            });
        }
    })
}

function placeOrder() {
    var orderId = $("#txt-id").val();
    var date = $("#txt-date").val();
    var customerId = $("#cmb-custId").val();

    var orderDetails = [];
    var rows = $("#tbl-orders tbody tr");

    for (var i = 1; i <= rows.length; i++) {
        // var code = $("#tbl-orders tbody:nth-child(i)").children("#td-code").text();
        var description;
        var quantity;
        var unitPrice;
        var total;
    }
}

function loadAllCustomers() {
    $.ajax({
        method: 'GET',
        url: "http://localhost:8080/pos/api/v1/customers"
    }).done(function (customers) {
        for (var i = 0; i < customers.length; i++) {
            var id = customers[i].id;
            var newOption = "<option>" + id + "</option>";
            $("#cmb-custId").append(newOption);
        }
    })
}

function loadAllItems() {
    $.ajax({
        method: 'GET',
        url: "http://localhost:8080/pos/api/v1/items"
    }).done(function (items) {
        for (var i = 0; i < items.length; i++) {
            var code = items[i].code;
            var newOption = "<option>" + code + "</option>";
            $("#cmb-code").append(newOption);
        }
    })
}

function loadCustomerName() {
    $.ajax({
        method: 'GET',
        url: 'http://localhost:8080/pos/api/v1/customers'
    }).done(function (customers) {
        for (var i = 0; i < customers.length; i++) {
            var id = customers[i].id;
            var name = customers[i].name;
            console.log($(this).val());
            if ($(this).val() === id) {
                $("#txt-name").text(name);
            }
        }
    })
}

function loadItemDescription() {
    $.ajax({
        method: 'GET',
        url: 'http://localhost:8080/pos/api/v1/items'
    }).done(function (items) {
        for (var i = 0; i < items.length; i++) {
            var code = items[i].code;
            var description = items[i].description;
            if ($("#cmb-custId option").val() === undefined) {
                return;
            } else {
                if ($("#cmb-custId option").val() === code) {
                    $("#txt-name").text(description);
                }
            }
        }
    })
}

function initializeTextFields() {
    var date = new Date();
    $("#txt-date").text(date);
}


