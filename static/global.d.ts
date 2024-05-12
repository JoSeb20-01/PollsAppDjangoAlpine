import { Alpine } from "alpinejs";

declare global {
    interface Window extends Window {
        Alpine: Alpine
    }
    
    const Alpine: Alpine;
}