
function validateForm() {
    const slPoint = document.getElementById('id_sl_point').value;
    const tpPoint = document.getElementById('id_tp_point').value;
    const lotSize = document.getElementById('id_lot_size').value;
    const priceInterval = document.getElementById('id_price_interval').value;
    const startButton = document.getElementById('start_button');
    const stopButton = document.getElementById('stop_button');
    
    if (slPoint && tpPoint && lotSize && priceInterval) {
        startButton.disabled = false;
    } else {
        startButton.disabled = true;
    }

    if (!startButton.disabled && !stopButton.disabled) {
        stopButton.disabled = true;
    }
}


document.addEventListener('DOMContentLoaded', function() {

    function fetchOrders() {
        fetch("/get_open_orders/")
            .then(response => response.json())
            .then(data => {
                const updateTable = (tableId, orders, totalProfit, isClosedOrders) => {
                    const tableBody = document.querySelector(`${tableId} tbody`);
                    tableBody.innerHTML = ""; // Clear existing rows
    
                    // Create a fragment to hold new rows
                    const fragment = document.createDocumentFragment();
    
                    orders.forEach(order => {
                        const row = document.createElement("tr");
    
                        const cells = [
                            order.symbol,
                            order.type === 0 ? "Buy" : "Sell",
                            order.volume,
                            isClosedOrders 
                            ? order.price.toFixed(3)
                            : order.price_open.toFixed(3),
                            ...(isClosedOrders ? [] : [order.sl, order.tp]),
                            order.profit.toFixed(3)
                        ];
    
                        cells.forEach(text => {
                            const cell = document.createElement("td");
                            cell.textContent = text;
                            row.appendChild(cell);
                        });
    
                        fragment.appendChild(row);
                    });
    
                    tableBody.appendChild(fragment);
                    
                    const colspan = isClosedOrders ? 4 : 6;
                    
                    const totalRow = document.createElement('tr');
                    totalRow.style.position = 'sticky';
                    totalRow.style.bottom = '0';
                    totalRow.style.backgroundColor = '#f4f4f4';
                    totalRow.style.borderTop = '2px solid #ddd';
                    totalRow.style.zIndex = '1';
                    
                    totalRow.innerHTML = `
                        <td colspan="${colspan}" style="text-align: right;"><strong>Total Profit</strong></td>
                        <td><strong>${totalProfit.toFixed(3)}</strong></td>
                    `;
                    tableBody.appendChild(totalRow);
                   
                };
    
                if (data.orders) {
                    updateTable("#orders-table", data.orders, data.total_open_profit, false);
                }
                if (data.closed_orders) {
                    updateTable("#orders-table-closed", data.closed_orders, data.total_close_profit, true);
                }
            })
            .catch(error => console.error('Error fetching orders:', error));
    }
    
    
    function fetchPrices() {
        fetch('/get_current_prices/')
            .then(response => response.json())
            .then(data => {
                document.getElementById('ask-price').textContent = data.ask;
                document.getElementById('bid-price').textContent = data.bid;
                document.getElementById('symbol').textContent = data.symbol;
                document.getElementById('account-balance').textContent = data.account_balance;
                // ocument.getElementById('account-id-display').textContent = 'Account ID: ' + data.account_id;
                
                // document.getElementById('difff').textContent = (data.ask-data.bid).toFixed(4);
            })
            .catch(error => console.error('Error fetching prices:', error));


    }
    
  

    // fetchAccountId();
    fetchOrders();
    fetchPrices();
    setInterval(fetchOrders, 1000); // Fetch orders every 1 sec
    setInterval(fetchPrices, 100); // Fetch prices every 0.1 seconds
});