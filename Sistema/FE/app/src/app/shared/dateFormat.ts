export const DATE_FORMAT = "yyyy-MM-dd"

export function formatDate(Date: Date): string{
    return `${Date.getFullYear()}-${Date.getMonth()<10 ? '0' + Date.getMonth() : Date.getMonth()}-${Date.getDay()<10 ? '0' + Date.getDay() : Date.getDay()}`;
}