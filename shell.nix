{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "gtk-examples-python";

  nativeBuildInputs = [
    pkgs.gobject-introspection
  ];

  buildInputs = [
    pkgs.gtk3
    pkgs.libhandy
    pkgs.libadwaita
    pkgs.gst_all_1.gstreamer
    (pkgs.python3.withPackages (p: with p; [
      pygobject3 gst-python
    ]))
  ];
}
