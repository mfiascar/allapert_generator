/*
 * Vairous tests to check the memebers of the Aperture class
 *
 * 
 *
 */

#include "ReadTwiss.h"
#include "Aperture.h"
#include "OneMetre.h"
//#include "AssignOneMetre.h"

int main ()
{
  double pi = (double)atan2(0.0, -1.0);

  Aperture A;

  // Check the constructor
  cout<<A.GetApertAlignX()<<endl;
  cout<<A.GetApertAlignY()<<endl;
  // Assign aperture and offset (case of D1.F)
  A.PutApert(0.064, 0.0265, 0.064, 0.0265);
  A.SetApertAlign(0.01396, 0.0);
  A.SetApertAlign(0.03, 0.02);
  //
  cout<<A.GetApertAlignX()<<endl;
  cout<<A.GetApertAlignY()<<endl;
  //
  A.PlotAperture("CheckD1.dat");
  //
  vector<double> x, y; // X and y are inverted!
  double x1 = -0.1,
    x2 = 0.1,
    y1 = -0.08,
    y2 = 0.08;
  int n_tot = 200,
    lost;
  for (int k = 0; k <= n_tot; k++){
    x.push_back( x1 + (x2-x1)/(double)n_tot * k );
    y.push_back( y1 + (y2-y1)/(double)n_tot * k );
  }
  ofstream out("IsLost.dat");
  out.precision(1);
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();
  out.open("IsLost_xy.dat"); // Save also the vector with the x-y coordinates
  out.precision(8);
  for (int k = 0; k <= n_tot; k++)
    out<<x[k]<<" "<<y[k]<<endl;
  out.close();
  /*
  % Matlab commands to plot the aperture:;
  load IsLost.dat;
  load IsLost_xy.dat;
  y= IsLost_xy(:,1);
  x= IsLost_xy(:,2);
  figure;surf(x,y,IsLost);
  */

  /*
  // Test rectangular aperture
  out.open("IsLostRectangle.dat", ios::out);
  A.empty();
  A.PutApert(0.03, 0.05, 0.0, 0.0);
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();

  cout<<A.GiveAperture(0.0)<<endl;
  cout<<A.GiveAperture(45)<<endl;
  cout<<A.GiveAperture(85)<<endl;

  A.PlotAperture("Rectangle.dat");
  */

  // Test aperture rotation
  A.empty();
  // Simple aperture
  A.PutApert(0.06, 0.03, 0.06, 0.03);
  out.open("IsLost_normal.dat");
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();
  // Traslation only
  A.SetApertAlign(0.01, 0.02);
  out.open("IsLost_trasl.dat");
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();
  // Angle only
  A.SetApertAlign(0.0, 0.0);
  A.SetAngle(30.0 * pi / 180);
  out.open("IsLost_angle.dat");
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();
  A.PutApert(0.12, 0.03, 0.0, 30.0);
  // Both angle and traslation
  A.SetApertAlign(0.01, 0.02);
  out.open("IsLost_both.dat");
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();

  A.empty();
  A.PutApert(0.0, 0.0, 0.015, 0.02);
  A.SetAngle(30.0);
  A.PlotAperture("RotatedAperture.dat");

  out.open("IsLostTiledAperture.dat", ios::out);
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();

  // Example of tilted collimator from the lattice:
  A.empty();
  A.PutApert(0.04, 0.00804623,  0.0, 40.7);
  //  A.PutApert(0.05, 0.02, 0.05, 0.02);
  cout<<A.GetAngle()<<endl;
  A.PlotAperture("Tilt.dat");
  out.open("IsLostTiledAperture.dat", ios::out);
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();

  // Check 'IsLost' function for a collimator
  A.empty();
  A.PutApert(0.04, 0.0046939, 0.0, 0.0116696);
  A.PlotAperture("TiltedColl.dat"); // (LHC[19790].GetAperture(0.0844)).PlotAperture("TiltedColl.dat");
  out.open("IsLostTiledAperture.dat", ios::out);
  for (int k = 0; k < x.size(); k++){
    for (int j = 0; j < y.size(); j++){
      lost = A.IsLost(x[k],y[j]);
      out<<setw(2)<<lost;
    }
    out<<endl;
  }
  out.close();

  return 0;
}



