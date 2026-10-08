#include <gtk/gtk.h>

int main(int argc, char **argv) {
    if (argc != 2 || !gtk_init_check(&argc, &argv)) return 2;
    gtk_rc_parse(argv[1]);
    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    GtkWidget *label = gtk_label_new("Hello, World!");
    gtk_widget_set_name(label, "greeting");
    gtk_container_add(GTK_CONTAINER(window), label);
    gtk_widget_show_all(window);
    GtkStyle *style = gtk_widget_get_style(label);
    GdkColor color = style->fg[GTK_STATE_NORMAL];
    if (color.red != 0x2020 || color.green != 0x3030 || color.blue != 0x4040) return 1;
    g_print("%s\n", gtk_label_get_text(GTK_LABEL(label)));
    gtk_widget_destroy(window);
    return 0;
}
