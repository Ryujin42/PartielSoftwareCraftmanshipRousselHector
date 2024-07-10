public class OrderProcessor {
    private Database database;
    private EmailService emailService;
    private InventorySystem inventorySystem;


    public OrderProcessor() {
        this.database = new Database();
        this.emailService = new EmailService();
        this.inventorySystem = new InventorySystem();
    }

    public void checkItemAvailability(Order order) {
        List<Item> items = order.getItems();
        for (Item item : items) {
            if (!inventorySystem.isItemAvailable(item)) {
                throw new RuntimeException("Item not available");
            }
        }
    }

    public void sendEmailToClient(Order order) {
        String message = "Your order has been received and is being processed.";
        emailService.sendEmail(order.getCustomerEmail(), "Order Confirmation", message);
    }

    public void updateInventory(Order order) {
        for (Item item : order.getItems()) {
            inventorySystem.updateInventory(item, item.getQuantity() * -1);
        }
    }

    public void applyDiscountToLoyalCustomer(Order order) {
        if (order instanceof LoyalCustomerOrder) {
            LoyalCustomerOrder loyalCustomerOrder = (LoyalCustomerOrder) order;
            loyalCustomerOrder.applyDiscount();
        }
    }


    public void processOrder(Order order) {
        checkItemAvailability(order);
        database.saveOrder(order);
        sendEmailToClient(order);
        updateInventory(order);
        applyDiscountToLoyalCustomer(order);
    }
}


public class LoyalCustomerOrder extends Order {
    @Override
    public void applyDiscount() {
        // Appliquer une remise de 10%
        setTotalPrice(getTotalPrice() * 0.9);
    }
}
